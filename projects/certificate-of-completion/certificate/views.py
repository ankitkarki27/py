from django.shortcuts import render
from .forms import CertificateForm
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings

def generate_certificate(request):
    cert_path = None

    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            # Collect form data
            name = form.cleaned_data['name']
            course_name = form.cleaned_data.get('course_name', 'Course')
            certificate_id = form.cleaned_data.get('certificate_id', f"cert{timezone.now().strftime('%Y%m%d%H%M%S')}")
            issued_at = form.cleaned_data.get('issued_at') or timezone.now()

            # File paths
            template_path = os.path.join(settings.MEDIA_ROOT, 'templates', 'certificate_template.png')
            output_dir = os.path.join(settings.MEDIA_ROOT, 'certificates')
            font_regular_path = os.path.join(settings.MEDIA_ROOT, 'certificates', 'fonts', 'arial.ttf')
            font_bold_path = os.path.join(settings.MEDIA_ROOT, 'certificates', 'fonts', 'arialbd.ttf')
            font_name_path = os.path.join(settings.MEDIA_ROOT, 'certificates', 'fonts', 'DancingScript-Regular.ttf')  # For Name (Script Font)

            try:
                # Validate template image exists
                if not os.path.exists(template_path):
                    raise FileNotFoundError(f"Certificate template not found at: {template_path}")

                # Ensure output directory exists
                os.makedirs(output_dir, exist_ok=True)

                # Load certificate template image
                img = Image.open(template_path)
                draw = ImageDraw.Draw(img)

                # Load fonts (with fallback to default if missing)
                def load_font(path, size):
                    try:
                        return ImageFont.truetype(path, size)
                    except Exception:
                        return ImageFont.load_default()

                # Font settings
                font_name = load_font(font_name_path, 80)        # Name - Fancy Script
                font_course = load_font(font_bold_path, 40)      # Course - Bold
                font_id = load_font(font_regular_path, 30)       # Certificate ID - Regular
                font_date = load_font(font_regular_path, 40)     # Date - Regular

                # Draw text on image (Adjust X/Y positions as per your template)
                draw.text((180, 240), f"Certificate ID: {certificate_id}", font=font_id, fill=(0, 0, 0))
                draw.text((170, 700), name, font=font_name, fill=(0, 0, 0))
                draw.text((170, 920), course_name, font=font_course, fill=(0, 0, 0))
                draw.text((170, 1000), f"Issued on: {issued_at.strftime('%Y-%m-%d')}", font=font_date, fill=(0, 0, 0))

                # Save certificate image
                filename = f"{name.split()[0]}_{certificate_id}.png"
                file_path = os.path.join(output_dir, filename)
                img.save(file_path, 'PNG')

                # Generate relative path for media URL
                rel_path = os.path.relpath(file_path, settings.MEDIA_ROOT)
                cert_path = os.path.join(settings.MEDIA_URL, rel_path).replace("\\", "/")

            except Exception as e:
                return render(request, 'certificate/index.html', {
                    'form': form,
                    'cert_path': cert_path,
                    'error_message': f"Certificate generation failed: {str(e)}"
                })

    else:
        form = CertificateForm()

    return render(request, 'certificate/index.html', {
        'form': form,
        'cert_path': cert_path
    })

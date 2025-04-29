from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import CertificateForm
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings

def generate_certificate(request):
    cert_path = None
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # Ensure the media directory exists
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)

            # Load certificate template
            template_path = os.path.join(settings.BASE_DIR, 'certificate/static/images/certificate_template.jpg')
            image = Image.open(template_path)

            # Draw text (e.g., name) onto the image
            draw = ImageDraw.Draw(image)

            # Use a system font if the custom font isn't found
            font_path = "C:\\Windows\\Fonts\\arial.ttf"  # Example for Windows, adjust for other OSes
            font = ImageFont.truetype(font_path, 60)

            # Add the user's name (You can adjust the position)
            draw.text((670, 740), name, font=font, fill="black")

            # Convert the image to RGB mode before saving as JPEG
            image = image.convert("RGB")

            # Save generated certificate as JPEG
            output_path = os.path.join(settings.MEDIA_ROOT, f"{name}_certificate.jpg")
            image.save(output_path, "JPEG")

            # Set the path to be used in the template
            cert_path = f"{settings.MEDIA_URL}{name}_certificate.jpg"
    else:
        form = CertificateForm()

    return render(request, 'certificate/index.html', {'form': form, 'cert_path': cert_path})

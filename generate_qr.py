import qrcode
import os

# Create QR code for WhatsApp contact
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://wa.me/258840447327')
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color='black', back_color='white')

# Save
output_path = r'odescomplicando.com\_assets\media\68009cc0f3998cee7118824c787aa8a6.png'
img.save(output_path, 'PNG')
print(f'QR Code generated successfully at: {output_path}')

from django.shortcuts import render
from .models import Qrcode_info, Orders
import qrcode
import os


def generate_qrcode(childname, parent, color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f'http://127.0.0.1:8000/qrcode/1')
    qr.make(fit=True)

    # Set the foreground and background colors
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")

    # Save the QR code to a file
    file_name = childname+parent+"_qrcode.png"
    img.save(file_name)


def qrcode_func(request):
    if request.POST:
        print("********************************")
        parent = request.POST['parent']
        childname = request.POST['childname']
        streetaddress = request.POST['streetaddress']
        phone = request.POST['phone']
        towncity = request.POST['towncity']
        postcode = request.POST['postcode']
        color = request.POST['color']
        generate_qrcode(childname, parent, color)
        print("user_id", request.user.id)
        qrcode_info_form = Qrcode_info(parent=parent, childname=childname,  streetaddress=streetaddress,
                                       towncity=towncity, postcode=postcode, phone=phone)
        qrcode_info_form.save()
        order_details_form = Orders(user_id=request.user.id, product_id=1)
        order_details_form.save()
        return render(request, 'checkout.html', {'img_url': "https://i.etsystatic.com/27325021/r/il/fd2255/4073351281/il_794xN.4073351281_g8ds.jpg"})

    return render(request, 'qrcode/qrcode_generation.html')


def qrcode_detail(request, qrcode_id):
    qrcode_details = Qrcode_info.objects.get(id=qrcode_id)
    scanid = request.GET.get('scanId', '')
    context = {'qrcode_details': qrcode_details, }
    return render(request, 'qrcode/qrcode_details.html', context)

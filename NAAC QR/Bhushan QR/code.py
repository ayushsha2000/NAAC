import qrcode

generate_image = qrcode.make('https://ayushsha2000.github.io/bhushan/')
# https://limitless-shelf-43049.herokuapp.com/getinternalOneSemesterFiveMarks/19btris010
generate_image.save('bhushan.png')
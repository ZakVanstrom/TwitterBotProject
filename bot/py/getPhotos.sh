cd icloudPics || exit 1
rm -r ./*
icloudpd --directory ./ \
    --username zakyre15@yahoo.com \
    --password MarenMagic85! \
    --recent 10 \
    --live-photo-size original \
    --skip-videos
exit 0
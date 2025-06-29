for img in *.png; do
	ffmpeg -i "$img" -vf palettegen palette.png
	ffmpeg -i "$img" -i palette.png -lavfi paletteuse "${img%.png}.gif"
	rm palette.png
done

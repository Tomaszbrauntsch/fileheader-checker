# Fileheader Checker
Checks the header of files and determinse if the file it is claiming to be (via the file extension) actually is that file.
<br>
<br>Note: this project is still under development and will be adding more headers and features in the future

## Setup
Install the required packets by using pip
```
pip3 install -r requirements.txt
```

## Deployment
When running this file, please include the file that needs to be checked as an argument
```
python3 filechecker.py myfile.fileextension
```

## File Extensions Currently Supported
```
jpg/jpeg, png, gif, tif, tiff, bmp, dib, webp
```
## Source(s)
[File signatures reference](https://en.wikipedia.org/wiki/List_of_file_signatures)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

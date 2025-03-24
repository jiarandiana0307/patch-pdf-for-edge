import os
import pypdf


def remove_openaction(infile, outfile) -> bool:
    writer = pypdf.PdfWriter(infile)
    if writer.open_destination is None:
        return False

    writer.open_destination = None
    writer.write(outfile)
    return True


def main():
    for filename in os.listdir():
        if not os.path.isfile(filename) or os.path.splitext(filename)[1].lower() != '.pdf':
            continue

        try:
            result = remove_openaction(filename, filename)
            if result:
                print('modified', filename)
            else:
                print('no need to modify', filename)
        except Exception as e:
            print('failed to modify pdf', filename, e)

    input('enter to exit...')


if __name__ == '__main__':
    main()
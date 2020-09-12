"""File camera capture sample."""
import zivid

def _main():
    print("heyyooo")
    print(zivid.environment.data_path())
    app = zivid.Application()
    camera = app.create_file_camera(
        str(zivid.environment.data_path()) + "/MiscObjects.zdf"
    )

    # Dpes not allow you to save anywhere else...(EB NOTE)
    with camera.capture() as frame:
        frame.save("results.zdf") 


if __name__ == "__main__":
    _main()

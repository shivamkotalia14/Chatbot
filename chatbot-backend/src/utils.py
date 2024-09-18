import traceback
from src.store import Store
import cv2
def recognize(camera, recognition):
    """Recognizes ASL fingerspelling within video stream"""
    output = None  # Initialize output to handle cases where no data is processed
    try:
        if not camera.isOpened():
            print("Error: Camera not found.")
            return output

        while True:
            try:
                success, image = camera.read()
                if not success:
                    print("Failed to capture image.")
                    continue

                # Process the image with the recognition object
                try:
                    image, updated, points, output = recognition.process(image)
                    
                except Exception as e:
                    print(f"Error processing image: {e}")
                    continue

                # Resize the image for display
                image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

                # Display the image
                cv2.imshow('ASL Recognition', image)

                # Check if 'q' key was pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except Exception as e:
                print(f"Unexpected error in loop: {e}")
                traceback.print_exc()
                break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
    finally:
        camera.release()
        cv2.destroyAllWindows()
    return Store.parsed
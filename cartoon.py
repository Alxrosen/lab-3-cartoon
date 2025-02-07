# missing import statements should be added here
import wikipedia
import cv2

from images import get_wikipedia_page_thumbnail_url, download_image_from_url

def prompt_for_image():
    search_results_arr = []
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.
    
    return url, page_name: str, str
    """
    search_query = input("Enter name of a personality: ")
    try:
        for i in range(3):
            search_results_arr.append(get_wikipedia_page_thumbnail_url(search_query))
            print("Here: ", search_results_arr[i])
        return 0
    except Exception as e:
        print(f"Error: Unable to find image for the given name: {e}")
        return None, None
    
def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """
    pass
    # TODO (and remove the pass statement above)


    
if __name__ == "__main__":
    prompt_for_image()


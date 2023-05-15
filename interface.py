from PIL import Image
import torch
from torchvision import transforms

model = torch.load('reddit_model.pth')

def prediction(image_path):
    # Define the transformation to apply to the input image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    
    image = Image.open(image_path).convert('RGB')

    # Apply the transformation to the input image
    image_tensor = transform(image)

    # Add a batch dimension to the image tensor
    image_tensor = image_tensor.unsqueeze(0)

    # Put the model in evaluation mode
    model.eval()

    # Make a prediction on the input image
    with torch.no_grad():
        output = model(image_tensor)

    # Get the predicted class index
    predicted_index = output.argmax().item()

    # Print the predicted class label
    class_labels = ['Drawing', 'Graffiti', 'ArtPorn', 'Art', 'StreetArt',
       'ComicBookArt', 'IDAP', 'Illustration', 'Painting', 'learnart',
       'Calligraphy', 'Watercolor', 'ArtefactPorn', 'ArtCrit'] 
    predicted_label = class_labels[predicted_index]
    print('Success is most likely in r/', predicted_label)
    



print("Welcome to ArtAgent! Please give us the art you want to publish and we'll direct you to the communities where our algorithm indicates your work will get the most traction: \n ")
cond = True
while cond:
    png_file = input("Enter File Path: ")
    prediction(png_file)
    prompt = input("Do you have any further works you'd like to be published?(y/n)" )
    if (prompt == "n"):
        print("Have a good day!")
        cond = False


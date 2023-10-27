from huggingface_hub import InferenceClient
import gradio as gr
from PIL import Image
from io import BytesIO

def main():
    client = InferenceClient(model='stabilityai/stable-diffusion-xl-base-1.0')

    def inference(prompt):
        pil_image = client.text_to_image(prompt)
        return pil_image

    demo = gr.Interface(
        fn=inference,
        inputs=gr.Textbox(lines=2, placeholder="Prompt Here..."),
        outputs="image",
        title = "Andrew's web page",
        description= """Welcome! This is a deployment of a text-to-image web app using AWS, Docker, and other technologies. 
        The main point of the project was to show that I can deploy things end-to-end as opposed to just build out machine
        learning models (of which I have a fair amount on my resume and Github). I may actually build a full model and do more
        of the technical work in a later project but for now my priorities are showing that I can deliver business value.

        WARNING: If you put in an inappropriate prompt, the model may output something equally inappropriate 
        and I can't (and won't) take responsibility for that. There are also bias issues at play. Please use this responsibly!
        
        More information on the underlying model can be found here: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0""",
        )

    demo.launch()

if __name__ == '__main__':
    main()
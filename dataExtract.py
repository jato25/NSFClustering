import re, os

def extract_abstract(text):

    pat_abstract = re.compile('Abstract.*',re.M|re.DOTALL)
    abstract = pat_abstract.findall(text)
    abstract = re.sub(r'[\n\t]', '', abstract[0])
    abstract = re.sub(r'[\s+]{2,}', ' ', abstract)

    return abstract[11:].strip()

def process_files():
    for root, _, filenames in os.walk(f".{os.sep}Data"):
        output_texts = []

        for file in filenames:
            if file.endswith('.txt'):

                with open(os.path.join(root, file),'r') as input:
                    raw_text = input.read()
                    
                output_texts.append(extract_abstract(raw_text))
        
        out_filename = root.split(os.sep)[-1]
        
        if output_texts:
            with open(os.path.join(".", "preparedData",f"{out_filename}.txt"), "w+") as output:
                output.write('\n'.join(output_texts))

if __name__ == "__main__":     
    process_files()
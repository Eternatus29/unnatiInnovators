import React, { useState ,useCallback, useEffect} from 'react';
import { useDropzone } from 'react-dropzone';
import useDebounce from './useDebounce';



const categories = [
  "Services Provided:",
  "Payment:",
  "Term:",
  "Confidentiality:",
  "Termination:",
  "Governing Law:",
  "Signatures:"
];
function FileUpload() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [highlightedText, setHighlightedText] = useState('');
  const [entities, setEntities] = useState([]);
  const [fileName, setFileName] = useState('');
  const [predicted_text,setprediction]=useState([]);
  const [loading, setLoading] = useState(false);
  const [isDragActive, setIsDragActive] = useState(false); 
  const [summerized_text, setSummary] = useState('');

  const [prevScrollPos, setPrevScrollPos] = useState(0);
  const [visible, setVisible] = useState(true);

  const handleScroll = useCallback(() => {
    const currentScrollPos = window.pageYOffset;
    setVisible(prevScrollPos > currentScrollPos || currentScrollPos < 10);
    setPrevScrollPos(currentScrollPos);
  }, [prevScrollPos]);

  const debouncedHandleScroll = useDebounce(handleScroll, 100);

  useEffect(() => {
    window.addEventListener('scroll', debouncedHandleScroll);
    return () => {
      window.removeEventListener('scroll', debouncedHandleScroll);
    };
  }, [debouncedHandleScroll]);

  const handleFileChange = useCallback((e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);
    setFileName(uploadedFile.name);
 
  }, []);





  const handleUpload = async () => {
    
   
    if(!file){
    
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    
    try {
   
      const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();

        setText(data.text);
        setEntities(data.entities); 
        setHighlightedText(data.highlighted_text);
        const filteredPredictedText = data.predicted_text.filter(item => item[0].trim() !== '');
        setprediction(filteredPredictedText);
        setSummary(data.summerized_text);
    
       
      }else {
        const errorData = await response.json();
        console.error('Error uploading file:', errorData.error);
      }
    }
   catch (error) {
      console.error('Error uploading file:', error);
    } finally{
      setLoading(false);
    }
  
  };



  
  const onDrop = useCallback((acceptedFiles, rejectedFiles, event) => {
    const uploadedFile = acceptedFiles[0];
    setFile(uploadedFile);
    setFileName(uploadedFile.name);
   
  }, []);

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    onDragEnter: () => setIsDragActive(true),
    onDragLeave: () => setIsDragActive(false),
    multiple: false,
  });
 
  const scrollToSection = (id) => {
    const element = document.querySelector(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    } else {
      console.error(`Element with id ${id} not found.`);
    }
  };

  const [isOpen, setIsOpen] = useState(false);

  const toggleNav = () => {
    setIsOpen(!isOpen);
  }
  return (
    <>
  
      <header className={`header ${visible ? 'visible' : 'hidden'}`} >
        <div className='heading'>
        <img src={`${process.env.PUBLIC_URL}/images/file.png`} alt="Logo" className="logo" />
        <h1>Business Contract Validation</h1>
        </div>
        <button className="nav-toggle" onClick={toggleNav}>
          <span></span>
          <span></span>
          <span></span>
        </button>
        <nav className={`nav ${isOpen ? 'show' : ''}`}>
          <ul>
            <li><a onClick={() => scrollToSection('.container')}>Home</a></li>
            <li><a onClick={() => scrollToSection('.extracted-text')}>Extracted text</a></li>
            <li><a onClick={() => scrollToSection('.highlighted-text')}>Highlighted Text</a></li>
            <li><a onClick={() => scrollToSection('.classify-text')}>Classification</a></li>
            <li><a onClick={() => scrollToSection('.summerized-text')}>Summary</a></li>

          </ul>
        </nav>
        </header>
        

    <div className="container">
         
    <h2 className="upload-heading">Upload Contract Here</h2>
      <div {...getRootProps({ className: `dropzone  ${isDragActive ? 'active' : ''}` })}>
        <input {...getInputProps()} onChange={handleFileChange} />
        {file ? (
          <div className="file-info">
            <img src={`${process.env.PUBLIC_URL}/images/icon.png`} alt="File icon" style={imageStyle}/>
            <p>{fileName}</p>
          </div>
        ) : (
          <p>Drag & drop a file here, or click to select files</p>
        )}
      </div>

        <button onClick={handleUpload} className="upload-button">Generate</button>


        {loading && (
        <>
          <div className="skeleton skeleton-nav"></div>
          <section id="extracted-text" className="extracted-text">
            <h3></h3>
            <div className="scroll-container">
              <div className="skeleton skeleton-text"></div>
              <div className="skeleton skeleton-text"></div>
              <div className="skeleton skeleton-text"></div>
            </div>
          </section>
          <section id="highlighted-text" className="highlighted-text">
            <h3></h3>
            <div className="scroll-container">
              <div className="skeleton skeleton-highlight"></div>
              <div className="skeleton skeleton-highlight"></div>
              <div className="skeleton skeleton-highlight"></div>
            </div>
          </section>
          <section id="highlighted-text" className="highlighted-text">
            <h3></h3>
            <div className="scroll-container">
              <div className="skeleton skeleton-highlight"></div>
              <div className="skeleton skeleton-highlight"></div>
              <div className="skeleton skeleton-highlight"></div>
            </div>
          </section>
          <section id="highlighted-text" className="highlighted-text">
            <h3></h3>
            <div className="">
              <div className="skeleton skeleton-highlight"></div>
              <div className="skeleton skeleton-highlight"></div>
              <div className="skeleton skeleton-highlight"></div>
            </div>
          </section>
        </>
      )}

        
    {!loading &&text && (
      <>
      <h3 className="extracttext">Extracted Text</h3>
      <div className="extracted-text">
     
      <div className="scroll-container">

        <pre>{text}</pre>
      </div>
      </div>
   
      </>
    )}
   

 

{!loading &&entities.length > 0 && (
      <>
      
      <h3>Name and Entity</h3>
       <div className="ner">
        <ul>
          {entities.map((entity, index) => (
            <li key={index}>{entity}</li>
          ))}
        </ul>
        
      </div>

      </>
    )}

    {!loading &&highlightedText && (
      <>
      <span id="highlighted-text"></span>
      {/* <section id="highlighted-text"> */}
      <h3  style={{margin:"0 0 30px 0"}}>Highlighted Text</h3>
      <div className='highlighted-text'>
      
   
      <div className="scroll-container ">
            <pre dangerouslySetInnerHTML={{ __html: HighlightText(highlightedText) }} />
          </div>
        </div>
          {/* </section> */}
      </>
    )}

{!loading &&predicted_text.length > 0 && (
      <>
       <h3 className='classify-text'>Text Classification</h3>
      <div className="classify" >
        <ul >
          {predicted_text.map((entity, index) => {
            console.log(entity)
            return (
              <li key={index}>{entity[0]} <span className='bold-bro'>{entity[1]}</span></li>
            )
            }
          )}
            </ul>
            </div>
            </>
    )}

{!loading &&summerized_text && (
      <>
      <h3>Summary</h3>
      <div className="summerized-text">
    
        <div className='content'>{summerized_text}</div>
      </div>

      </>
    )}
    

  </div>
  
  </>
  );
}


const HighlightText = (text) => {
  let highlightedHtml = text;
  categories.forEach(category => {
    const regex = new RegExp(`\\b${category}`, 'gi');
    highlightedHtml = highlightedHtml.replace(regex, `<span class="highlighted">${category}</span>`);
  });
  return highlightedHtml;
};

const imageStyle = {
  maxWidth: '100px',
  maxHeight: '100px',
};
export default FileUpload;

# Gemini Java Optimizer

## Introduction
The **Gemini Java Optimizer** is a powerful Python-based tool that leverages Google Vertex AI's **Gemini model** to analyze, optimize, and stabilize Java **Spring Boot** projects. Additionally, it generates **JUnit 5** test cases to ensure robust testing and maintainability.

## Features
- **Code Optimization**: Enhances Java Spring Boot code for better readability, stability, and performance while preserving logic, inputs, and outputs.
- **Unit Test Generation**: Automatically generates **JUnit 5** test cases with **Mockito** for better test coverage.
- **Seamless Integration**: Reads Java files from a given file path and processes them using Vertex AI.
- **Preserves Functionality**: Ensures that API contracts and service logic remain unchanged while improving code quality.

## Prerequisites
To use this tool, ensure that you have the following setup:

1. **Google Cloud Project** with Vertex AI enabled.
2. **Python 3.8+** installed.
3. **Google Cloud SDK** configured with authentication.
4. Required Python libraries:
   ```bash
   pip install google-cloud-aiplatform vertexai
   ```

## Usage
### 1. Configure Your Google Cloud Project
Replace the placeholders in `main.py` with your **Google Cloud Project ID** and **Region**:
```python
vertexai.init(project="YOUR_PROJECT_ID", location="YOUR_REGION")
```

### 2. Provide the Java File Path
Update the `file_path` variable in `main.py` with the actual path to your **Spring Boot** Java file:
```python
file_path = "path/to/your/SpringBootFile.java"  # Replace with actual file path
```

### 3. Run the Script
Execute the Python script:
```bash
python main.py
```

### 4. View Optimized Code & Unit Tests
After execution, the optimized Java code and generated JUnit test cases will be displayed in the console.

## Example
### **Input Java Code**
```java
@RestController
public class ExampleController {
    @GetMapping("/add")
    public int add(@RequestParam int a, @RequestParam int b) {
        return a + b;
    }
}
```

### **Optimized Output**
```java
@RestController
public class ExampleController {
    @GetMapping("/add")
    public ResponseEntity<Integer> add(@RequestParam int a, @RequestParam int b) {
        return ResponseEntity.ok(Math.addExact(a, b));
    }
}
```

### **Generated JUnit Test Case**
```java
@SpringBootTest
class ExampleControllerTest {
    @Autowired
    private ExampleController controller;
    
    @Test
    void testAdd() {
        assertEquals(5, controller.add(2, 3));
    }
}
```

## Notes
- The tool does **not** change the logic, inputs, or outputs of the original Java code.
- If the provided Java file does not exist, an error message will be displayed.
- If unsure about any optimization, Gemini will provide a **reasonable suggestion** while preserving the core logic.

## License
This project is licensed under the **MIT License**.

## Contributing
Feel free to submit pull requests or issues for enhancements!

---
**Developed with ❤️ using Google Vertex AI & Python**


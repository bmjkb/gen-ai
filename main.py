from vertexai.language_models import TextGenerationModel
import vertexai
import os

def get_gemini_response(prompt, input_code):
    """
    Sends a request to the Gemini model on Vertex AI and returns the response.
    """
    vertexai.init(project="YOUR_PROJECT_ID", location="YOUR_REGION")
    model = TextGenerationModel.from_pretrained("gemini-pro")
    response = model.predict(prompt + "\n\n" + input_code)
    return response.text if response else "Error: No response received"

def read_java_file(file_path):
    """
    Reads the Java file content from the given file path.
    """
    if not os.path.isfile(file_path):
        return "Error: File not found"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def optimize_java_code(java_code):
    """
    Optimizes and stabilizes the given Java Spring Boot code using Gemini on Vertex AI.
    """
    prompt = (
        "System Prompt:\n"
        "Introduction: This task involves optimizing Java Spring Boot code for better performance, stability, and readability.\n"
        "Instructions: Analyze the given Java Spring Boot code, eliminate redundancies, improve efficiency, and apply best coding practices. Ensure compliance with modern Spring Boot standards.\n"
        "Goal: The optimization should not alter the logic, inputs, or outputs of the original code. It should maintain API contracts and service functionality.\n"
        "Constraints: The optimized code must maintain the original functionality, follow Java and Spring Boot best practices, and avoid unnecessary complexity.\n"
        "Examples:\n"
        "Input: @RestController public class ExampleController { @GetMapping(\"/add\") public int add(@RequestParam int a, @RequestParam int b) { return a + b; } }\n"
        "Output: @RestController public class ExampleController { @GetMapping(\"/add\") public ResponseEntity<Integer> add(@RequestParam int a, @RequestParam int b) { return ResponseEntity.ok(Math.addExact(a, b)); } }\n"
        "Tone and Style: Keep responses clear, structured, and professional.\n"
        "Fallback: If unsure, provide a reasonable optimization suggestion while preserving the core logic.\n"
    )
    return get_gemini_response(prompt, java_code)

def generate_unit_tests(java_code):
    """
    Generates JUnit test cases for the given Java Spring Boot code using Gemini on Vertex AI.
    """
    prompt = (
        "System Prompt:\n"
        "Introduction: This task requires generating JUnit test cases for a given Java Spring Boot class to ensure full test coverage.\n"
        "Instructions: Analyze the Java Spring Boot code and create unit tests covering normal cases, edge cases, and exception handling where applicable. Use Mockito for dependency mocking where necessary.\n"
        "Goal: The unit tests should validate the correctness of the original logic without modifying its behavior.\n"
        "Constraints: The tests should use JUnit 5 and Mockito, follow best testing practices, and ensure proper assertions.\n"
        "Examples:\n"
        "Input: @RestController public class ExampleController { @GetMapping(\"/add\") public int add(@RequestParam int a, @RequestParam int b) { return a + b; } }\n"
        "Output: @SpringBootTest class ExampleControllerTest { @Autowired private ExampleController controller; @Test void testAdd() { assertEquals(5, controller.add(2, 3)); } }\n"
        "Tone and Style: Keep responses precise, structured, and professional.\n"
        "Fallback: If unsure, generate the most comprehensive test cases possible based on the given logic.\n"
    )
    return get_gemini_response(prompt, java_code)

def main():
    file_path = "path/to/your/SpringBootFile.java"  # Replace with actual file path
    java_code = read_java_file(file_path)
    
    if "Error" in java_code:
        print(java_code)
        return
    
    optimized_code = optimize_java_code(java_code)
    test_cases = generate_unit_tests(optimized_code)
    
    print("Optimized Java Code:\n", optimized_code)
    print("\nGenerated Unit Tests:\n", test_cases)

if __name__ == "__main__":
    main()

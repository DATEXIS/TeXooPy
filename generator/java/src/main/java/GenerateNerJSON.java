import de.datexis.model.Document;
import de.datexis.preprocess.DocumentFactory;

public class GenerateNerJSON {
  public static void main(String[] args) {
    Document foo = DocumentFactory.fromText("foo");
    System.out.println(foo);
    //TODO Implement an example that covers cases for our NER use case
    //TODO export to JSON
  }

}

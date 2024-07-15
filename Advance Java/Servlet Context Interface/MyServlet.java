import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/myservlet")
public class MyServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Get the servlet context
        ServletContext servletContext = getServletContext();

        // Get the attribute from the servlet context
        String attribute = (String) servletContext.getAttribute("exampleAttribute");

        // Send the attribute as a response
        response.getWriter().write(attribute);
    }
}

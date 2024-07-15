import javax.servlet.ServletContext;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

public class MyServletContextListener implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent servletContextEvent) {
        // This method is called when the servlet context is initialized (started)

        // Get the servlet context
        ServletContext servletContext = servletContextEvent.getServletContext();

        // Set an attribute in the servlet context
        servletContext.setAttribute("exampleAttribute", "Hello from ServletContextListener");
    }

    @Override
    public void contextDestroyed(ServletContextEvent servletContextEvent) {
        // This method is called when the servlet context is about to be destroyed (stopped)
    }
}

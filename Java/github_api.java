import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils;
import org.eclipse.egit.github.core.RepositoryContents;
import org.eclipse.egit.github.core.service.ContentsService;
import org.eclipse.egit.github.core.service.GitHubService;
import org.eclipse.egit.github.core.service.RepositoryService;

public class GitHubUploader {

    public static void main(String[] args) throws IOException {
        // Initialize variables with GitHub credentials and file details
        String username = "YOUR_GITHUB_USERNAME";
        String password = "YOUR_GITHUB_PASSWORD";
        String repositoryName = "YOUR_REPOSITORY_NAME";
        String branchName = "master";
        String filePath = "PATH_TO_FILE";
        String commitMessage = "YOUR_COMMIT_MESSAGE";

        // Create a new file object
        File file = new File(filePath);

        // Initialize GitHub service and repository service
        GitHubService gitHubService = new GitHubService();
        gitHubService.getClient().setCredentials(username, password);
        RepositoryService repositoryService = new RepositoryService(gitHubService.getClient());

        // Find the repository to upload to
        RepositoryContents rootContents = repositoryService.getContents(username, repositoryName, branchName);

        // Create a new contents service and add the file to the repository
        ContentsService contentsService = new ContentsService(gitHubService.getClient());
        RepositoryContents contents = new RepositoryContents();
        contents.setName(file.getName());
        contents.setPath(file.getName());
        contents.setContent(FileUtils.readFileToString(file));
        contents.setType("file");
        contents.setMessage(commitMessage);
        contentsService.createFile(rootContents.getSha(), contents);

        System.out.println("File uploaded successfully!");
    }
}

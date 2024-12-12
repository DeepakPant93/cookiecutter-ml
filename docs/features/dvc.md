### Data Version Control (DVC) with Google Drive as Remote Storage

In this application, we are using **DVC** (Data Version Control) to track changes in our data. DVC allows us to version control large data files, enabling easy collaboration and versioning of datasets. For this application, we are using **Google Drive** as the remote storage for DVC.

### Setting Up Google Drive as Remote Storage for DVC

To use Google Drive as a remote storage in DVC, follow these steps:

1. **Create a Folder in Google Drive**
   Create a new folder in your Google Drive where the data will be stored.

2. **Set Folder Permissions**
   Change the folder's permissions to **"Anyone with the link"** and grant **read and write** access to allow DVC to interact with the folder.

3. **Get Folder ID**
   The folder ID will be part of the Google Drive folder URL (e.g., `https://drive.google.com/drive/folders/<folder_id>`). Use this folder ID as the `data_source_id` for the application.

4. **Install Google Cloud SDK**
   Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) on your local machine to manage authentication and interact with Google Cloud services.

5. **Create a Service Account**
   After installing the Google Cloud SDK, create a service account and assign the necessary permissions to access Google Drive.

6. **Run DVC Setup Command**
   Run the following command to set up Google Drive as the remote storage for DVC:

```bash
make bake-dvc
```

This command will configure DVC to use your Google Drive folder as the remote storage.

### Using DVC to Manage Data

Once the remote storage is set up, you can start managing your data using DVC. The following commands are used to add, push, and pull data:

-   **Add Data to DVC**:
    Add a data file to both DVC and Git, and enable auto-stage in DVC:

```bash
dvc add <data_file>
```

-   **Push Data to Git and DVC Remote**:
    Push the changes to both Git and the remote storage (Google Drive):

```bash
dvc push
```

-   **Pull Data from Git and DVC Remote**:
    Pull the data from both Git and the remote storage:

```bash
dvc pull
```

### Running the DVC Pipeline

To execute the DVC pipeline, use the following command. The pipeline will run the code specified in the `dvc.yaml` file:

```bash
dvc run <pipeline_name>
```

This will trigger the pipeline defined in the `dvc.yaml` file, where various steps and commands for data processing and training are outlined.

---

### Conclusion

With these steps, you can effectively use DVC for managing and versioning your data in Google Drive. By integrating DVC with your workflow, you can ensure reproducibility and collaboration in managing large datasets.

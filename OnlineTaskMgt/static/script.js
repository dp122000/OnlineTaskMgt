// Function to confirm project removal
function confirmRemoveProject(projectId, projectName) {
    const confirmation = confirm(`Are you sure you want to remove the project "${projectName}"?`);
    if (confirmation) {
        // Redirect to the remove project URL (e.g., /remove_project/123)
        window.location.href = `/remove_project/${projectId}`;
    }
}

// Function to confirm project update
function confirmUpdateProject(projectId) {
    const confirmation = confirm("Are you sure you want to update this project?");
    if (confirmation) {
        // Redirect to the edit project URL (e.g., /edit_project/123)
        window.location.href = `/edit_project/${projectId}`;
    }
}

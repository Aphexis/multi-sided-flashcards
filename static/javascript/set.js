function delete_set(view_only){
    if (window.confirm("You are deleting a set. This will remove all data associated with this set! " +
        "Are you sure you want to do this?")) {
        window.location.replace(location.pathname + "/delete");
    }
}


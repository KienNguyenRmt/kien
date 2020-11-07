Sub list_files_recursive()
'List all files that are located under a selected folder
    Dim obj_file_system As Object
    Dim str_folder As String
    Dim int_last_row as Integer

    str_folder = mod_list_files_recursive.get_folder
    Set obj_file_system = CreateObject("Scripting.FileSystemObject")
    int_last_row = ActiveWorkbook.ActiveSheet.Range("A1").CurrentRegion.Rows.Count
    ActiveWorkbook.ActiveSheet.Cells(int_last_row, 1).Resize(1, 3) = Array("Name", "Creation Date", "Path")
    mod_list_files_recursive.explore_folders obj_file_system.get_folder(str_folder), ActiveWorkbook.Name, ActiveSheet.Name
End Sub

Function explore_folders(arr_cur_folder As Variant, str_my_wb As String, str_sheet_name As String)
    Dim int_last_row As Long

    For Each SubFolder In arr_cur_folder.SubFolders
        mod_list_files_recursive.explore_folders SubFolder, str_my_wb, str_sheet_name
    Next

    For Each file In arr_cur_folder.Files
        int_last_row = Workbooks(str_my_wb).Sheets(str_sheet_name).Range("A1").CurrentRegion.Rows.Count + 1
        Workbooks(str_my_wb).Sheets(str_sheet_name).Cells(int_last_row, 1).Value2 = file.Name
        Workbooks(str_my_wb).Sheets(str_sheet_name).Cells(int_last_row, 2).Value2 = file.DateCreated
        Workbooks(str_my_wb).Sheets(str_sheet_name).Cells(int_last_row, 3).Value2 = file.Path
    Next
End Function

Function get_folder() As String
    Dim fldr As FileDialog
    Dim str_item As String
    Set fldr = Application.FileDialog(msoFileDialogFolderPicker)
    With fldr
        .Title = "Select a Folder"
        .AllowMultiSelect = False
        .InitialFileName = Application.DefaultFilePath
        If .Show <> -1 Then GoTo NextCode
        str_item = .SelectedItems(1)
    End With
NextCode:
    If Right(str_item, 1) <> "\" Then
        str_item = str_item & "\"
    End If
    get_folder = str_item
    Set fldr = Nothing
End Function
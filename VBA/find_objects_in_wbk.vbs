Sub find_object()
    'Loop through sheet and figure if the object is created.'
    Dim obj_counter As ListObject           
    Dim shtCounter As Worksheet
    Dim NewRow As Variant
 
    Set obj_table_1 = Nothing
    
    For Each shtCounter In ActiveWorkbook.Sheets
        If shtCounter.ListObjects.Count > 0 Then
            For Each obj_counter In shtCounter.ListObjects
                If obj_counter.Name Like "table_1" Then 'Assume that your object is named table_1'
                    Set objOvw = ActiveWorkbook.Sheets(shtCounter.Name).ListObjects("table_1")
                End If
            Next
        End If
        If Not obj_table_1 Is Nothing Then Exit For
    Next
    
    If obj_table_1 Is Nothing Then
        MsgBox "Your object is not presented in this workbook!."
        End
    End If

End sub
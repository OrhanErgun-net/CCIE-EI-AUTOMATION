var responseInJson = pm.response.json();
var template = `
    <style type="text/css">
        .tftable {font-size:14px;color:#333333;width:100%;border-width: 1px;border-color: #87ceeb;border-collapse: collapse;}
        .tftable th {font-size:18px;color:#e0ffff;background-color:#e41c1c;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;text-align:left;}
        .tftable tr {background-color:#ffffff;}
        .tftable td {font-size:14px;border-width: 1px;padding: 8px;border-style: solid;border-color: #87ceeb;}
        .tftable tr:hover {background-color:#e0ffff;}
    </style>
    
    <table class="tftable" border="1">
        <tr>
            <th>Host Name</th>
            <th>Device ID</th>
        </tr>
        
        {{#each response.data}}
            <tr>
                <td>{{host-name}}</td>
                <td>{{deviceId}}</td>
            </tr>
        {{/each}}
    </table>
`;

pm.visualizer.set(template, {
    response: responseInJson
});
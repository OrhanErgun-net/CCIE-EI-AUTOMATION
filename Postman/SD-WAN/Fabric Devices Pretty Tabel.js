var responseInJson = pm.response.json();

var template = `
    <table>
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
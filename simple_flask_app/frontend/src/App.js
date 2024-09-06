import React, { useEffect, useState } from 'react';

function App() {
    const [data, setData ] = useState(null)

    useEffect(() => {
        fetch('/hello')
            .then(response => response.json())
            .then(data => setData(data.data));
    }, []);

    return (
        <div>
            <h1>{data}</h1>
        </div>
    );
}

export default App;
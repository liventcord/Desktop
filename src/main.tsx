// src/App.js
import React, { useEffect } from 'react';
import { Webview } from '@tauri-apps/api/webview';

const App = () => {
  useEffect(() => {
    const webview = new Webview(null, 'uniqueLabel', {
      url: 'http://localhost:3000',  // This can be a path to an HTML file or a remote URL
    });

    webview.once('tauri://created', () => {
      console.log('Webview created');
    });
    webview.once('tauri://error', (e) => {
      console.log('Webview error:', e);
    });

    webview.emit('some-event', 'data');
    const unlisten = webview.listen('event-name', (e) => {
      console.log('Received event:', e);
    });
    unlisten();
  }, []);

  return (
    <div>
      <h1>Hello from React and Tauri!</h1>
    </div>
  );
};

export default App;

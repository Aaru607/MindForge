import { useState } from "react";
import { api } from "../services/api";
export default function AdminUpload() {
  const [file, setFile] = useState(null);
  const upload = async () => {
    const data = new FormData();
    data.append("file", file);
    await api.post("/careers/admin/upload/", data);
    alert("Upload successful");
  };
  return (
    <div>
      <h2>Admin Upload</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={upload}>Upload</button>
    </div>
  );
}

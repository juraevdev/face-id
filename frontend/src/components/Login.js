import React, { useState } from "react";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api/v1";

const Login = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setFile(e.target.files[0]);
      console.log("Selected file:", e.target.files[0]); // 🔍 Fayl tanlanganini tekshirish
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setMessage("Please select an image first!");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("face_image", file); // ❗ `face_image` nomi backendga mos!

    try {
      const response = await axios.post(`${API_BASE_URL}/accounts/register/`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log("Response:", response.data);
      setMessage(`Face ID check passed! User ID: ${response.data.user_id}`);
    } catch (error) {
      console.error("Error response:", error.response?.data);
      setMessage("Face ID check failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Face ID Login</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} required />
        <button type="submit" disabled={loading}>
          {loading ? "Checking..." : "Submit"}
        </button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default Login;
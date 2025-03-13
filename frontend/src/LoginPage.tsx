import React, { useState } from 'react';
import 'antd/dist/reset.css';

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleMenuClick = () => {

  };

  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h2 className="text-2xl font-bold mb-4">Login</h2>
        <p className="text-gray-600 mb-6">to get started</p>
        <input
          type="email"
          placeholder="Email"
          className="block w-full p-2 border border-gray-300 rounded mb-4"
          value={email}
          onChange={(e) => setEmail(e.target.value)} // Update email state
        />
        <input
          type="password"
          placeholder="Password"
          className="block w-full p-2 border border-gray-300 rounded mb-4"
          value={password}
          onChange={(e) => setPassword(e.target.value)} // Update password state
        />
        <div className="text-right mb-4">
          <a href="#" className="text-blue-500 hover:underline text-sm">
            Forgot Password?
          </a>
        </div>
        <button
          className="bg-blue-600 text-white w-full py-2 rounded hover:bg-blue-700"
          onClick={handleMenuClick}
        >
          Continue
        </button>
        <p className="text-center text-sm mt-4">

        </p>
      </div>
    </div>
  );
};

export default LoginPage;

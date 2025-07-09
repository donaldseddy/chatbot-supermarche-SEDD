import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // ton API Django locale

export const getAllProducts = async () => {
    const response = await axios.get(`${API_URL}/products/`);
    return response.data;
};

export const getProductById = async (id: string) => {
    const response = await axios.get(`${API_URL}/products/${id}/`);
    return response.data;
};

export const deleteProduct = async (id: string) => {
    const response = await axios.delete(`${API_URL}/products/${id}/`);
    return response.data;
};

import api from './api';

export interface Message {
  id?: number;
  sender_id: number;
  receiver_id: number;
  content: string;
  timestamp?: string;
}

export interface ConversationPreview {
  partner_id: number;
  partner_name: string;
  partner_image?: string;
  last_message?: string;
  last_message_time?: string;
  unread_count?: number;
  is_online?: boolean;
}

export const getChatHistory = async (partnerId: number) => {
  const response = await api.get<Message[]>(`/chat/history/${partnerId}`);
  return response.data;
};

export const getConversations = async () => {
  const response = await api.get<ConversationPreview[]>('/chat/conversations');
  return response.data;
};

// Helper to get the WebSocket URL with authentication
export const getWebSocketUrl = (userId: number) => {
  const token = localStorage.getItem('token');
  // Note: WebSockets use 'ws://' instead of 'http://'
  return `ws://localhost:8000/chat/ws/${userId}/${token}`;
};
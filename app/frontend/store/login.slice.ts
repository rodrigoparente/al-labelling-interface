import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Login } from "../../sdk/@types/Login";

interface LoginSliceState {
  isLogged: boolean;
  username: string;
  userToken: string;
}

const initialState: LoginSliceState = {
  isLogged: false,
  username: '',
  userToken: ''
}

const loginSlice = createSlice({
  name: 'login',
  initialState,
  reducers: {
    addToken(state, action:PayloadAction<Login.isLogged>) {
      state.isLogged = action.payload.isLogged
      state.username = action.payload.username
      state.userToken = action.payload.userToken
    }
  },
});

export const loginReducer = loginSlice.reducer;
export const { addToken } = loginSlice.actions;
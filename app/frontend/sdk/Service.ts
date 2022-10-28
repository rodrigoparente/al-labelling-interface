import axios, { AxiosResponse } from "axios"

const Http = axios.create()


class Service {
  protected static Http = Http
  protected static getData = getData
}

function getData<T> (res: AxiosResponse<T>) {
  return res.data
}

Http.defaults.baseURL = 'http://201.49.62.134:8080'

export default Service
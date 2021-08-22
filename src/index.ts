/// <reference types="@types/google.maps" />

import { User } from './components/User';
import { Company } from './components/Company';
import { Map } from './components/Map';

const user = new User();
const company = new Company();
const customMap = new Map("map");

customMap.addMarker(user);
customMap.addMarker(company);
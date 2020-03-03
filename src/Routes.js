import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Login from './Login';

export default function Routes() {
  return (
    <Switch>
      <Route path='/login' exact component={Login} />

    </Switch>
  );
}
// <Route path="/login" exact component={Login} />
// export CONST Login= '/login';

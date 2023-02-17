import { addMessages, init, getLocaleFromNavigator } from 'svelte-i18n';

import en from '../locales/en.json';
import fr from '../locales/fr.json';

addMessages('en', en);
addMessages('en-US', en);
addMessages('fr', fr);

init({
	fallbackLocale: 'en',
	initialLocale: getLocaleFromNavigator()
});

function get(id: string): ReturnType<typeof cy.get> {
	return cy.get(`[data-cy="${id}"]`)
}

const IMAGE_URL = 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6'
const AUTHOR_URL = 'https://unsplash.com/@cenali'

describe('Basic flow', () => {
	beforeEach(() => {
		cy.viewport('macbook-13')
	})

	it('Should render the fruit gallery correctly', () => {
		cy.visit('/')
		cy.location('pathname').should('eq', '/')

		get('FruitCard').should('have.length', 6)
		get('FruitCardImage')
			.first()
			.should('have.attr', 'src')
			.and('contain', IMAGE_URL)
		get('FruitImageAuthor')
			.first()
			.should('have.text', 'Matheus Cenali')
			.and('have.attr', 'href', AUTHOR_URL)
			.click()
		get('FruitCardName').first().should('have.text', 'Apple')
	})

	it('Should navigate to the details page on click', () => {
		get('FruitCardName').first().click()
		cy.location('pathname').should('eq', `/apple`)
	})

	it('Should go back to gallery on back button click', () => {
		get('BackLink').click()
		cy.location('pathname').should('eq', '/')
	})

	it('Should navigate to the details page on enter', () => {
		get('FruitCard').first().focus().type('{enter}')
		cy.location('pathname').should('eq', `/apple`)
	})

	it('Should render the fruit details correctly', () => {
		get('FruitImage').should('have.attr', 'src').and('contain', IMAGE_URL)
		get('FruitName').should('have.text', 'Apple')
	})

	it('Should render a error message', () => {
		cy.viewport('iphone-xr')
		cy.intercept('/fruits', request => request.destroy()).as('getFruits')
		cy.reload()
		cy.wait('@getFruits')
		get('LoadingOrError').should('have.text', 'Failed to fetch')
	})

	it('Should redirect to gallery when trying to access a invalid fruit', () => {
		cy.visit('/cypress')
		cy.location('pathname').should('eq', '/')
	})
})

import { Vue, Component } from 'nuxt-property-decorator'
import _ from 'lodash'
import { Dictionary } from 'vue-router/types/router'

type QueryParams = Dictionary<string | (string | null)[] | null | undefined>

@Component
export class TaskManagerMixin extends Vue {
  /**
   * Is the given program currently opened
   * @param programId The id which identifies the target program
   */
  protected isActive (programId: string): boolean {
    return this.$route.query[programId] !== undefined
  }

  /**
   * Is the given program currently on top of the window hierarchy
   * @param programId THe id which identifies the target program
   */
  protected isOnTop (programId: string): boolean {
    // find the program which is on top
    const top = _.reduce(this.query, (akk, value, key) => {
      const numVal = Number(value)
      if (numVal < akk.index) {
        return { id: key, index: numVal }
      }
      return akk
    }, { id: '', index: Number.MAX_SAFE_INTEGER })

    return top.id === programId
  }

  /**
   * Open the given program and place it on top of the window hierarchy
   * @param programId The id which identifies the target program
   */
  protected openProgram (programId: string): void {
    const query = this.lowerAllPrograms(this.query)
    query[programId] = '1'
    this.$router.replace({ query })
  }

  /**
   * Close the given program so that it is not displayed anymore
   * @param programId The id which identifies the target program
   */
  protected closeProgram (programId: string): void {
    const query: QueryParams = { ...this.$route.query }
    delete query[programId]
    this.$router.replace({ query })
  }

  /**
   * Raise an already open program to the top of the window hierarchy
   * @param programId The id which identifies the target program
   */
  protected raiseProgram (programId: string): void {
    if (!this.isActive(programId)) {
      throw new Error(`program ${programId} is not opened and therefore cannot be raised`)
    }

    const query = this.lowerAllPrograms(this.query)
    query[programId] = '1'
    this.$router.replace({ query })
  }

  /**
   * Get the current query parameters but as an object which can safely be passed to `$router.replace({ query })`
   * without raising DuplicateNavigation errors
   */
  private get query (): QueryParams {
    return { ...this.$route.query }
  }

  /**
   * Lower all programs by increasing their respective query parameter by one.
   *
   * This effectively makes room for a new program that can be brought to the top.
   */
  private lowerAllPrograms (query: QueryParams): QueryParams {
    // @ts-ignore because the type definition for lodash is incorrect here
    return _.mapValues(query, (value: string) => {
      const numVal = Number(value)
      if (Number.isNaN(numVal)) {
        return value
      } else {
        return String(numVal + 1)
      }
    })
  }
}

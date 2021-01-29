import { Vue, Component } from 'nuxt-property-decorator'
import _ from 'lodash'
import { Dictionary, RawLocation, Route } from 'vue-router/types/router'

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
   * @param programId The id which identifies the target program
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
   * Is the given program currently in a minimized state so that only the header is visible
   * @param programId The id which identifies the target program
   */
  protected isProgramMinimized (programId: string): boolean {
    return this.$route.query[`${programId}_min`] === 'true'
  }

  /**
   * Is the given program currently in a maximized state so that it fills the whole viewport
   * @param programId The id which identifies the target program
   */
  protected isProgramMaximized (programId: string): boolean {
    return this.$route.query[`${programId}_max`] === 'true'
  }

  /**
   * Get the window hierarchy index of the given program
   * @param programId The id which identifies the target program
   */
  protected getProgramIndex (programId: string): number {
    if (!this.isActive(programId)) {
      throw new Error(`program ${programId} is not opened and therefore has no index`)
    }

    return Number(this.query[programId])
  }

  /**
   * Open the given program and place it on top of the window hierarchy
   * @param programId The id which identifies the target program
   */
  protected openProgram (programId: string): void {
    const query = this.lowerAllPrograms(this.query)
    query[programId] = '1'
    delete query[`${programId}_max`]
    delete query[`${programId}_min`]
    this.navigate({ query })
  }

  /**
   * Close the given program so that it is not displayed anymore
   * @param programId The id which identifies the target program
   */
  protected closeProgram (programId: string): void {
    const query: QueryParams = { ...this.$route.query }
    delete query[programId]
    delete query[`${programId}_max`]
    delete query[`${programId}_min`]
    this.navigate({ query })
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
    this.navigate({ query })
  }

  /**
   * Minimize an already open program so that only the titlebar is visible
   * @param programId The id which identifies the target program
   */
  protected minimizeProgram (programId: string): void {
    const query = this.query
    query[`${programId}_min`] = 'true'
    delete query[`${programId}_max`]
    this.navigate({ query })
  }

  /**
   * Revert program minimization so that it is displayed normally
   * @param programId The id which identifies the target program
   */
  protected unminimizeProgram (programId: string): void {
    const query = this.query
    delete query[`${programId}_min`]
    this.navigate({ query })
  }

  /**
   * Maximize an already open program so that only the titlebar is visible
   * @param programId The id which identifies the target program
   */
  protected maximizeProgram (programId: string): void {
    const query = this.query
    query[`${programId}_max`] = 'true'
    delete query[`${programId}_min`]
    this.navigate({ query })
  }

  /**
   * Revert program maximization so that it is displayed normally
   * @param programId The id which identifies the target program
   */
  protected unmaximizeProgram (programId: string): void {
    const query = this.query
    delete query[`${programId}_max`]
    delete query[`${programId}_min`]
    this.navigate({ query })
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

  /**
   * Execute navigation to new query parameters while ignoring DuplicateNavigation errors
   * @param location Target Location
   */
  private navigate (location: RawLocation): Promise<void | Route> {
    return this.$router.replace(location).catch((reason) => {
      if (reason.name === 'NavigationDuplicated') {
        return
      }
      throw reason
    })
  }
}

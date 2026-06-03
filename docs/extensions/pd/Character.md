---
search:
  boost: 10.0
---

# Class: Character 


_Information about character in the public sphere_



<div data-search-exclude markdown="1">



URI: [pd:Character](https://w3id.org/lmodel/dpv/pd/Character)





```mermaid
 classDiagram
    class Character
    click Character href "../Character/"
      PublicLife <|-- Character
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [PublicLife](PublicLife.md)
        * **Character**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Character](https://w3id.org/lmodel/dpv/pd/Character) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Character




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Character |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Character |
| native | pd:Character |
| exact | dpv_pd:Character, dpv_pd_owl:Character |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Character
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Character
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about character in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Character
exact_mappings:
- dpv_pd:Character
- dpv_pd_owl:Character
is_a: PublicLife
class_uri: pd:Character

```
</details>

### Induced

<details>
```yaml
name: Character
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Character
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about character in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Character
exact_mappings:
- dpv_pd:Character
- dpv_pd_owl:Character
is_a: PublicLife
class_uri: pd:Character

```
</details></div>
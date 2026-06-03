---
search:
  boost: 10.0
---

# Class: Interaction 


_Information about interactions in the public sphere_



<div data-search-exclude markdown="1">



URI: [pd:Interaction](https://w3id.org/lmodel/dpv/pd/Interaction)





```mermaid
 classDiagram
    class Interaction
    click Interaction href "../Interaction/"
      PublicLife <|-- Interaction
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [PublicLife](PublicLife.md)
        * **Interaction**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Interaction](https://w3id.org/lmodel/dpv/pd/Interaction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Interaction




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Interaction |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Interaction |
| native | pd:Interaction |
| exact | dpv_pd:Interaction, dpv_pd_owl:Interaction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Interaction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Interaction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about interactions in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Interaction
exact_mappings:
- dpv_pd:Interaction
- dpv_pd_owl:Interaction
is_a: PublicLife
class_uri: pd:Interaction

```
</details>

### Induced

<details>
```yaml
name: Interaction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Interaction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about interactions in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Interaction
exact_mappings:
- dpv_pd:Interaction
- dpv_pd_owl:Interaction
is_a: PublicLife
class_uri: pd:Interaction

```
</details></div>
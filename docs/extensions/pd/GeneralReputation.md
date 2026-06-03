---
search:
  boost: 10.0
---

# Class: GeneralReputation 


_Information about reputation in the public sphere_



<div data-search-exclude markdown="1">



URI: [pd:GeneralReputation](https://w3id.org/lmodel/dpv/pd/GeneralReputation)





```mermaid
 classDiagram
    class GeneralReputation
    click GeneralReputation href "../GeneralReputation/"
      PublicLife <|-- GeneralReputation
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [PublicLife](PublicLife.md)
        * **GeneralReputation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:GeneralReputation](https://w3id.org/lmodel/dpv/pd/GeneralReputation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* General Reputation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#GeneralReputation |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:GeneralReputation |
| native | pd:GeneralReputation |
| exact | dpv_pd:GeneralReputation, dpv_pd_owl:GeneralReputation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneralReputation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#GeneralReputation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about reputation in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- General Reputation
exact_mappings:
- dpv_pd:GeneralReputation
- dpv_pd_owl:GeneralReputation
is_a: PublicLife
class_uri: pd:GeneralReputation

```
</details>

### Induced

<details>
```yaml
name: GeneralReputation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#GeneralReputation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about reputation in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- General Reputation
exact_mappings:
- dpv_pd:GeneralReputation
- dpv_pd_owl:GeneralReputation
is_a: PublicLife
class_uri: pd:GeneralReputation

```
</details></div>
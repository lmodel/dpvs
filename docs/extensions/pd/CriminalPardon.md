---
search:
  boost: 10.0
---

# Class: CriminalPardon 


_Information about criminal pardons_



<div data-search-exclude markdown="1">



URI: [pd:CriminalPardon](https://w3id.org/lmodel/dpv/pd/CriminalPardon)





```mermaid
 classDiagram
    class CriminalPardon
    click CriminalPardon href "../CriminalPardon/"
      Criminal <|-- CriminalPardon
        click Criminal href "../Criminal/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Criminal](Criminal.md)
        * **CriminalPardon**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CriminalPardon](https://w3id.org/lmodel/dpv/pd/CriminalPardon) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Criminal Pardon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CriminalPardon |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CriminalPardon |
| native | pd:CriminalPardon |
| exact | dpv_pd:CriminalPardon, dpv_pd_owl:CriminalPardon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CriminalPardon
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalPardon
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal pardons
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Pardon
exact_mappings:
- dpv_pd:CriminalPardon
- dpv_pd_owl:CriminalPardon
is_a: Criminal
class_uri: pd:CriminalPardon

```
</details>

### Induced

<details>
```yaml
name: CriminalPardon
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalPardon
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal pardons
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Pardon
exact_mappings:
- dpv_pd:CriminalPardon
- dpv_pd_owl:CriminalPardon
is_a: Criminal
class_uri: pd:CriminalPardon

```
</details></div>
---
search:
  boost: 10.0
---

# Class: Fetish 


_Information about an individual's sexual fetishes_



<div data-search-exclude markdown="1">



URI: [pd:Fetish](https://w3id.org/lmodel/dpv/pd/Fetish)





```mermaid
 classDiagram
    class Fetish
    click Fetish href "../Fetish/"
      Sexual <|-- Fetish
        click Sexual href "../Sexual/"
      
      
```





## Inheritance
* [Sexual](Sexual.md) [ [External](External.md)]
    * **Fetish**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Fetish](https://w3id.org/lmodel/dpv/pd/Fetish) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Fetish




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Fetish |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Fetish |
| native | pd:Fetish |
| exact | dpv_pd:Fetish, dpv_pd_owl:Fetish |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Fetish
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Fetish
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about an individual's sexual fetishes
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Fetish
exact_mappings:
- dpv_pd:Fetish
- dpv_pd_owl:Fetish
is_a: Sexual
class_uri: pd:Fetish

```
</details>

### Induced

<details>
```yaml
name: Fetish
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Fetish
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about an individual's sexual fetishes
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Fetish
exact_mappings:
- dpv_pd:Fetish
- dpv_pd_owl:Fetish
is_a: Sexual
class_uri: pd:Fetish

```
</details></div>
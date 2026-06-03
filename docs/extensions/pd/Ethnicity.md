---
search:
  boost: 10.0
---

# Class: Ethnicity 


_Information about ethnic origins and lineage_



<div data-search-exclude markdown="1">



URI: [pd:Ethnicity](https://w3id.org/lmodel/dpv/pd/Ethnicity)





```mermaid
 classDiagram
    class Ethnicity
    click Ethnicity href "../Ethnicity/"
      External <|-- Ethnicity
        click External href "../External/"
      

      Ethnicity <|-- EthnicOrigin
        click EthnicOrigin href "../EthnicOrigin/"
      Ethnicity <|-- Race
        click Race href "../Race/"
      

      
```





## Inheritance
* [External](External.md)
    * **Ethnicity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Ethnicity](https://w3id.org/lmodel/dpv/pd/Ethnicity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Ethnicity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Ethnicity |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Ethnicity |
| native | pd:Ethnicity |
| exact | dpv_pd:Ethnicity, dpv_pd_owl:Ethnicity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ethnicity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Ethnicity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about ethnic origins and lineage
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Ethnicity
exact_mappings:
- dpv_pd:Ethnicity
- dpv_pd_owl:Ethnicity
is_a: External
class_uri: pd:Ethnicity

```
</details>

### Induced

<details>
```yaml
name: Ethnicity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Ethnicity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about ethnic origins and lineage
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Ethnicity
exact_mappings:
- dpv_pd:Ethnicity
- dpv_pd_owl:Ethnicity
is_a: External
class_uri: pd:Ethnicity

```
</details></div>
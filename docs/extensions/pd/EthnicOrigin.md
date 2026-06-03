---
search:
  boost: 10.0
---

# Class: EthnicOrigin 


_Information about ethnic origin_



<div data-search-exclude markdown="1">



URI: [pd:EthnicOrigin](https://w3id.org/lmodel/dpv/pd/EthnicOrigin)





```mermaid
 classDiagram
    class EthnicOrigin
    click EthnicOrigin href "../EthnicOrigin/"
      Ethnicity <|-- EthnicOrigin
        click Ethnicity href "../Ethnicity/"
      
      
```





## Inheritance
* **EthnicOrigin** [ [Ethnicity](Ethnicity.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EthnicOrigin](https://w3id.org/lmodel/dpv/pd/EthnicOrigin) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Ethnic Origin




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EthnicOrigin |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EthnicOrigin |
| native | pd:EthnicOrigin |
| exact | dpv_pd:EthnicOrigin, dpv_pd_owl:EthnicOrigin |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EthnicOrigin
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EthnicOrigin
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about ethnic origin
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Ethnic Origin
exact_mappings:
- dpv_pd:EthnicOrigin
- dpv_pd_owl:EthnicOrigin
mixins:
- Ethnicity
class_uri: pd:EthnicOrigin

```
</details>

### Induced

<details>
```yaml
name: EthnicOrigin
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EthnicOrigin
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about ethnic origin
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Ethnic Origin
exact_mappings:
- dpv_pd:EthnicOrigin
- dpv_pd_owl:EthnicOrigin
mixins:
- Ethnicity
class_uri: pd:EthnicOrigin

```
</details></div>
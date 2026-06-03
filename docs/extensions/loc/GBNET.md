---
search:
  boost: 10.0
---

# Class: GBNET 


_Concept representing region City of Newcastle upon Tyne in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-NET](https://w3id.org/lmodel/dpv/loc/GB-NET)





```mermaid
 classDiagram
    class GBNET
    click GBNET href "../GBNET/"
      GB <|-- GBNET
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBNET**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-NET](https://w3id.org/lmodel/dpv/loc/GB-NET) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-NET
* City of Newcastle upon Tyne




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-NET |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-NET |
| native | loc:GBNET |
| exact | dpv_loc:GB-NET, dpv_loc_owl:GB-NET |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBNET
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NET
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Newcastle upon Tyne in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NET
- City of Newcastle upon Tyne
exact_mappings:
- dpv_loc:GB-NET
- dpv_loc_owl:GB-NET
is_a: GB
class_uri: loc:GB-NET

```
</details>

### Induced

<details>
```yaml
name: GBNET
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-NET
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region City of Newcastle upon Tyne in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-NET
- City of Newcastle upon Tyne
exact_mappings:
- dpv_loc:GB-NET
- dpv_loc_owl:GB-NET
is_a: GB
class_uri: loc:GB-NET

```
</details></div>
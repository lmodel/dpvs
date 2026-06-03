---
search:
  boost: 10.0
---

# Class: GBBRC 


_Concept representing region Borough of Bracknell Forest in country_

_United Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-BRC](https://w3id.org/lmodel/dpv/loc/GB-BRC)





```mermaid
 classDiagram
    class GBBRC
    click GBBRC href "../GBBRC/"
      GB <|-- GBBRC
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBBRC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-BRC](https://w3id.org/lmodel/dpv/loc/GB-BRC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-BRC
* Borough of Bracknell Forest




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-BRC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-BRC |
| native | loc:GBBRC |
| exact | dpv_loc:GB-BRC, dpv_loc_owl:GB-BRC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBBRC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BRC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Bracknell Forest in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BRC
- Borough of Bracknell Forest
exact_mappings:
- dpv_loc:GB-BRC
- dpv_loc_owl:GB-BRC
is_a: GB
class_uri: loc:GB-BRC

```
</details>

### Induced

<details>
```yaml
name: GBBRC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-BRC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Borough of Bracknell Forest in country

  United Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-BRC
- Borough of Bracknell Forest
exact_mappings:
- dpv_loc:GB-BRC
- dpv_loc_owl:GB-BRC
is_a: GB
class_uri: loc:GB-BRC

```
</details></div>
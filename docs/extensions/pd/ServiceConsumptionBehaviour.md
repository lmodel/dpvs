---
search:
  boost: 10.0
---

# Class: ServiceConsumptionBehaviour 


_Information about the consumption of a service, e.g. time and duration_

_of consumption_



<div data-search-exclude markdown="1">



URI: [pd:ServiceConsumptionBehaviour](https://w3id.org/lmodel/dpv/pd/ServiceConsumptionBehaviour)





```mermaid
 classDiagram
    class ServiceConsumptionBehaviour
    click ServiceConsumptionBehaviour href "../ServiceConsumptionBehaviour/"
      Behavioural <|-- ServiceConsumptionBehaviour
        click Behavioural href "../Behavioural/"
      

      ServiceConsumptionBehaviour <|-- TVViewingBehaviour
        click TVViewingBehaviour href "../TVViewingBehaviour/"
      

      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **ServiceConsumptionBehaviour**
            * [TVViewingBehaviour](TVViewingBehaviour.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ServiceConsumptionBehaviour](https://w3id.org/lmodel/dpv/pd/ServiceConsumptionBehaviour) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Service Consumption Behaviour




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ServiceConsumptionBehaviour |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ServiceConsumptionBehaviour |
| native | pd:ServiceConsumptionBehaviour |
| exact | dpv_pd:ServiceConsumptionBehaviour, dpv_pd_owl:ServiceConsumptionBehaviour |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceConsumptionBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ServiceConsumptionBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about the consumption of a service, e.g. time and duration

  of consumption'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Service Consumption Behaviour
exact_mappings:
- dpv_pd:ServiceConsumptionBehaviour
- dpv_pd_owl:ServiceConsumptionBehaviour
is_a: Behavioural
class_uri: pd:ServiceConsumptionBehaviour

```
</details>

### Induced

<details>
```yaml
name: ServiceConsumptionBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ServiceConsumptionBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about the consumption of a service, e.g. time and duration

  of consumption'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Service Consumption Behaviour
exact_mappings:
- dpv_pd:ServiceConsumptionBehaviour
- dpv_pd_owl:ServiceConsumptionBehaviour
is_a: Behavioural
class_uri: pd:ServiceConsumptionBehaviour

```
</details></div>